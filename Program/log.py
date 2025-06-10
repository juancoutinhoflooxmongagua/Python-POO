class Log:
    def log(self, msg):
        return self._log(msg)

    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    l = LogFileMixin()
    l.log('qualquer coisa')
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('Que legal')
