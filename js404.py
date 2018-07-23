from subprocess import Popen, PIPE
from urlparse import urlparse
import argparse

def main(args):
  jserrors = get_404_js_calls(args.u)
  jserrors = jserrors.split('\n')
  positive_results=[]

  for jserror in jserrors:
        if not is_valid_url(jserror):
              continue
        domain = get_domain_from_string(jserror)
        if  domain_existence_check(domain) is False:
              publish_result(domain + ' <<< doesnt exist!', positive_results)
              publish_result("full error: " + jserror, positive_results)
  if args.o:
    write_results_to_file(positive_results, args.o)

def write_results_to_file(results, file):
  if len(results) < 1:
    return

  outfile = open(file, 'w')
  for result in results:
    print >> outfile, result    
    
def publish_result(string, list_of_outputs):
      list_of_outputs.append(string)
      print(string)


def is_valid_url(url):
    try:
      result = urlparse(url)
      return all([result.scheme, result.netloc, result.path])
    except:
      return False

def get_404_js_calls(url):
  process = Popen(["phantomjs", "--web-security=no", "--ssl-protocol=any", "--ignore-ssl-errors=yes", "ph.js", url], stdout=PIPE,stderr=PIPE)
  (output, err) = process.communicate()
  exit_code = process.wait()
  return output

def get_domain_from_string(input_string):
  domain=input_string.split("//")[-1].split("/")[0]
  return domain

def domain_existence_check(domain):
  process = Popen(["host", domain], stdout=PIPE,stderr=PIPE)
  (output, err) = process.communicate()
  exit_code = process.wait()

  if 'not found' in output:
        return False
  else:
        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Check for misspelled or expired external JS calls')

    parser.add_argument('-o', metavar = 'output', type = str,
                    help = 'Output file to write to', required = False)
   
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', metavar = 'URL', type = str,
                    help = 'Single URL to scan', required = True)
    
    args = parser.parse_args()

    main(args)