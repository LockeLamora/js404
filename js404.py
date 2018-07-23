from subprocess import Popen, PIPE

process = Popen(["phantomjs", "--web-security=no", "--ssl-protocol=any", "--ignore-ssl-errors=yes", "ph.js", "https://cnn.com"], stdout=PIPE,stderr=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
print(output)
