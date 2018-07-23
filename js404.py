from subprocess import Popen, PIPE
from urlparse import urlparse
import argparse

def main(args):
  print("Searching for invalid external JS paths")    
  scan_for_js_errors(args.u, args.w, args.o)

def scan_for_js_errors(single, multiple, output):
      jserrors = []
      if single is not None:
            jserrors.append(get_404_js_calls(single))
            interpret_results(jserrors, single, output)
      if multiple is not None:
            urls = open(multiple).read().splitlines()
            for url in urls:
                  print ("try " + url)
                  jserrors.append(get_404_js_calls(url))
                  interpret_results(jserrors, url, output)
                  jserrors.pop

def interpret_results(jserrors, url, output):
      for jserror in jserrors:
            if not is_valid_url(jserror):
                  continue
            domain = get_domain_from_string(jserror)
            if  domain_existence_check(domain) is False:
                        publish_result(domain + ' <<< doesnt exist!', output)
                        publish_result("full error: " + jserror, output)
                        publish_result("from URL: " + url, output)
                        publish_result("=" * 30, output)

def write_results_to_file(results, file):
      if len(results) < 1:
            return

      outfile = open(file, 'a+')
      print >> outfile, results    
    
def publish_result(string, output):
      if output:
            write_results_to_file(string, output)
      print(string)


def is_valid_url(url):
    try:
      result = urlparse(url)
      return all([result.scheme, result.netloc, result.path])
    except:
      return False

def get_404_js_calls(url):
      try:    
            process = Popen(["phantomjs", "--web-security=no", "--ssl-protocol=any", "--ignore-ssl-errors=yes", "ph.js", url], stdout=PIPE,stderr=PIPE)
            (output, err) = process.communicate()
            exit_code = process.wait()
            return output
      except:
            return

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
   
    parser.add_argument('-u', metavar = 'URL', type = str,
                    help = 'Single URL to scan', required = False)

    parser.add_argument('-w', metavar = 'url_list', type = str,
                    help = 'A file containing multiple URLs to scan', required = False)
    
    args = parser.parse_args()

    main(args)