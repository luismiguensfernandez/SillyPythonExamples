import beanstalkc


def produce():
    command = 'echo Hello world!'
    beanstalk = beanstalkc.Connection(host='localhost', port=11300)
    beanstalk.put(command)

if __name__ == '__main__':
    produce()


