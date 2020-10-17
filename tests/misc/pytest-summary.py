import json
import sys


def load_report(filename):
    report = []
    with open(filename, "r") as f:
        for line in f:
            result = json.loads(line)
            if result["$report_type"] == "TestReport" and result["when"] == "call":
                report.append(result)
            if (
                result["$report_type"] == "CollectReport"
                and result["outcome"] == "failed"
            ):
                result["outcome"] = "errors"  # pytest report shows error
                report.append(result)

    return report


def print_report(report):
    summary = {}
    for row in report:
        if row["outcome"] not in summary:
            summary[row["outcome"]] = 0
        summary[row["outcome"]] += 1

    summary_text = ', '.join([f"{v} {k}" for k, v in summary.items()])

    print("Results: " + summary_text)


def main():
    filename = sys.argv[1]
    report = load_report(filename)
    print_report(report)


if __name__ == '__main__':
    main()
