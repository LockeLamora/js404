from subprocess import Popen, PIPE

process = Popen(["phantomjs", "ph.js", "https://partnerize.bamboohr.co.uk/login.php"], stdout=PIPE)
(output, err) = process.communicate()
print(output)
exit_code = process.wait()