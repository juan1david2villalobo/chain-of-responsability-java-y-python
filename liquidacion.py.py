class ReportFormat(object):
    PDF = 0
    TEXT = 1


class Report(object):
    """liquidacion."""

    def __init__(self, format_):
        self.title = 'pago de nomina en proceso'
        self.text = ['pago dependiendo si es de planta, administartivo o contratado']
        self.format_ = format_


class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)


class TipoProfesor(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.PDF:
            self.output_report(request.title, request.text)
        else:
            super(TipoProfesor, self).handle(request)

    def output_report(self, title, text):
        print '<html>'
        print '  <head>'
        print '    <title>%s</title>' % title
        print '  </head>'
        print '  <body>'
        for line in text:
            print '    <p>%s</p>' % line
        print '  </body>'
        print '</html>'


class nomina(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.TEXT:
            self.output_report(request.title, request.text)
        else:
            super(nomina, self).handle(request)

    def output_report(self, title, text):
        print 5*'*' + title + 5*'*'
        for line in text:
            print line


class noPago(Handler):

    def handle(self, request):
        print "no tiene tiempo trabajado"


if __name__ == '__main__':
    report = Report(ReportFormat.TEXT)
    pdf_handler = TipoProfesor()
    text_handler = nomina()

    pdf_handler.nextHandler = text_handler
    text_handler.nextHandler = noPago()

    pdf_handler.handle(report)
