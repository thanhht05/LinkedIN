import time
from follow_linked import click_follow
from Linked_job import get_latest_job
from api_golike import complete_job, skip_job
from config import ACCOUNT_ID
from color import GREEN, RESET, RED, BLUE, YELLOW
from get_info_job import check_type
from like_linkedIn import safe_like


def main():
    cookie = input("Nhập cookie: ")
    n = int(input("Nhập số lần muốn chạy: "))

    price = 0
    time_success = 0
    for i in range(1, n + 1):
        print(f"\n=== Lần {i}/{n} ===")
        job_data = get_latest_job()
        if not job_data:
            print("[-] Không có job để thực hiện, chờ 5 giây...")
            time.sleep(5)
            continue

        if (
            check_type(job_data["link"]) == "COMPANY"
            or check_type(job_data["link"]) == "PROFILE"
        ):
            success = click_follow(cookie, job_data)
        else:
            success = safe_like(cookie, job_data)

        if success:
            if complete_job(job_data):
                price += job_data["price_after_cost"]
                print(f"{BLUE}[+] Total price: {price}{RESET}")
                time_success += 1
            else:
                print(f"{RED}[!] complete_job thất bại, gửi report...")
                skip_job(job_data)
        else:
            print(f"{RED}[!] Job bị lỗi!{RESET}")
            skip_job(job_data)

        print(f"{GREEN}[+] Hoàn tất lần {time_success} / {n}{RESET}")
        print(f"[*] Đợi 5 giây trước khi job tiếp theo...", end="", flush=True)
        for j in range(10):
            print(".", end="", flush=True)
            time.sleep(1)
        print(" ✅")


if __name__ == "__main__":
    main()
