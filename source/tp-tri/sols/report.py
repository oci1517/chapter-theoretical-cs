class Format(object):

    name = 'Undefined'

    def __init__(self):
        self.result = ''

    def add_row(self, row):
        self.result += row + '\n'

class FormatRST(Format):
    name = 'RST'
    def rst(self, caption, headers, rows, sep=';'):
        num_spaces = 3
        return '\n'.join([
            '.. csv-table:: ' + caption,
            ' '*num_spaces + ':header: ' + ','.join(['"' + h + '"' for h in headers ]),
            ' '*num_spaces + ':delim: ' + sep,
            ' '*num_spaces,
        ]) + '\n' + '\n'.join([' '*num_spaces + sep.join(map( str, r)) for r in rows])

    def output(self, report, options=None):
        options = options or {}
        options['caption'] = options.get('caption', '<caption here>')
        options['sep'] = options.get('sep', ';')

        return self.rst(options['caption'], report.headers, report.data, options['sep'])



class FormatCSV(Format):
    name='CSV'
    def format_row(self, row, sep=";"):
        return sep.join([str(f) for f in row])

    def output(self, report, options=None):
        options = options or {}

        self.add_row(self.format_row(report.headers))

        for d in report.data:
            self.add_row(self.format_row(d))

        return self.result






class FormatSTDOUT(Format):
    name = 'STDOUT'
    def output(self, report, options=None):
        options = options or {}

        for row in report.data:
            for (i, field) in enumerate(report.headers):
                self.add_row()
                print(field, " : ", row[i], sep=" // ")




class Report(object):

    def __init__(self, headers=None):
        self.headers = headers
        self.data = []
        self.formats = []
        self.output = ''

    def insert(self, data):
        if len(self.headers) > 0 and len(data) != len(self.headers):
            raise ValueError('number of data fields does not match header length')

        self.data += [data]

    def add_format(self, formatter):
        self.formats += [formatter]

        return self

    def add_formats(self, formatters):
        for f in formatters:
            self.add_format(f)

        return self

    def report(self):
        self.output = '\n\n'.join(
            [str(f.name) + '\n' + len(f.name)*'=' + '\n' + f().output(report=self) for f in self.formats]
        )

        return self

    def stdout(self):
        print(self.output)

def to_excel(number):
    return str(number).replace(".", ",")

# vieille fonction auxiliaire permettant de régler le format de sortie, cette fonction
# est appelée par la fonction bench
def report(data, output):

    if "screen" == output:
        print("N = ", N, " : time", elapsed, "seconds")
    if "csv" == output:
        print("{};{}".format(N, to_excel(elapsed)))
    if "tabs" == output:
        print("{}\t{}".format(N, elapsed))
    if "csvfile" == output:
        with open("bench.csv", "a") as fd:
            fd.write("{};{}".format(N, elapsed))
