import requests
import csv

def get_branch_details(ifsc):
    url = f"https://ifsc.razorpay.com/{ifsc}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_csv(ifsc_list, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['IFSC', 'MICR', 'BRANCH', 'ADDRESS', 'STATE', 'CONTACT', 'UPI', 'RTGS', 'CITY', 'CENTRE', 'DISTRICT', 'NEFT', 'IMPS', 'SWIFT', 'ISO3166', 'BANK', 'BANKCODE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ifsc in ifsc_list:
            branch_details = get_branch_details(ifsc)
            if branch_details:
                writer.writerow(branch_details)

if __name__ == "__main__":
    branches_file = 'branches.csv'
    ifsc_list = []
    with open(branches_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ifsc_list.append(row['IFSC'])

    
    output_file = 'branch_details.csv'
    generate_csv(ifsc_list, output_file)
    print(f"CSV file '{output_file}' generated successfully.")
