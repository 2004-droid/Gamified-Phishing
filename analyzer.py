import csv

def run_analysis():
    def read_csv_rows(path):
        try:
            with open(path, mode='r') as file:
                return list(csv.reader(file))
        except FileNotFoundError:
            return []

    sent_rows = read_csv_rows('emails_sent.csv')
    data_rows = read_csv_rows('data.csv')

    total_sent = len(sent_rows)
    total_captured = len(data_rows)
    risk_percent = (total_captured / total_sent * 100) if total_sent > 0 else 0

    print("\n" + "="*40)
    print("         RTA SIMULATION REPORT")
    print("="*40)
    print(f"Emails Sent:       {total_sent}")
    print(f"Successful Captures: {total_captured}")
    print(f"Company Risk:      {risk_percent:.1f}%")
    print("-" * 40)

    if data_rows:
        print("LATEST ACTIVITY:")
        for row in data_rows[-3:]:
            print(f"- User '{row[0]}' clicked at {row[2]}")
    else:
        print("LATEST ACTIVITY: No captures yet.")

    print("="*40)

if __name__ == "__main__":
    run_analysis()