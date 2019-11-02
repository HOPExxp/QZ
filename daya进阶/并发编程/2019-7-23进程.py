
# import subprocess
#
# run_progress = subprocess.run(['dir'],shell=True)
# print(run_progress.returncode)
#
#
# import subprocess
# print("in and out:")
#
# proc = subprocess.Popen(
#     ['dir',r"C:\apk"],
#     stdin= subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     shell = True
# )
# msg = "massge:".encode("gbk")
# stdout_value = proc.communicate(msg)[0].decode("gbk")
# stdin = proc.stdin
# print(stdin)
# print("Path:",repr(stdout_value))

# #单进程  in 1
# import subprocess
# print("in and out:")
#
# proc = subprocess.Popen(
#     ['dir'],
#     stdin= subprocess.PIPE,
#     shell = True
# )
# msg = "massge:".encode('utf-8')
# proc.communicate(msg)

#单进程  in 2
import subprocess

print('write:')
proc = subprocess.Popen(
    ['dir'],
    stdin=subprocess.PIPE,
    shell = True
)

#*****************    input没起作用？？？？？？
proc.communicate()