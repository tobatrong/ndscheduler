"""A job to run executable programs."""


from subprocess import PIPE,STDOUT, Popen
from ndscheduler import job

class ShellJob(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': ('This will run an executable program. You can specify as many '
                      'arguments as you want. This job will pass these arguments to the '
                      'program in order.'),
            'arguments': [
                {'type': 'string', 'description': 'Executable path'}
            ],
            'example_arguments': '["/usr/local/my_program", "--file", "/tmp/abc", "--mode", "safe"]'
        }

    def run(self, *args, **kwargs):
        p = Popen(list(args), stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True)
        output, err = p.communicate("input data that is passed to subprocess' stdin")
        rc={}
        if not output:
           raise Exception(err)
      
        
        return {'returncode': p.returncode,'result':output}


if __name__ == "__main__":
    # You can easily test this job here
    job = ShellJob.create_test_instance()
    job.run('ls', '-l')
