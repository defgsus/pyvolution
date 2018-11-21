

class Table:
    """
    Simple table to dump values
    """
    def __init__(self, headers):
        self.headers = headers
        self.rows = []

    def add_row(self, row):
        if len(row) != len(self.headers):
            raise IndexError("Number of columns (%s) different to number of headers (%s)" % (
                len(row), len(self.headers)
            ))
        self.rows.append(row)

    def get_column_widths(self):
        widths = dict()
        for x, name in enumerate(self.headers):
            widths[name] = max(
                max(len(str(row[x])) for row in self.rows) if self.rows else 1,
                len(name),
            )
        return widths

    def sort_by_column(self, x, key=None):
        if key is None:
            self.rows.sort(key=lambda row: row[x])
        else:
            self.rows.sort(key=lambda row: key(row[x]))

    def dump(self, fp=None, spacing=2):
        if fp is None:
            import sys
            fp = sys.stdout
        widths = self.get_column_widths()
        fmt_str = " ".join("%%%ss" % (widths[name]-1+spacing) for name in self.headers) + "\n"
        fp.write(fmt_str % tuple(self.headers))
        for row in self.rows:
            fp.write(fmt_str % tuple(row))

