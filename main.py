import time  # To utilize time.sleep we must import time, standard library.
import urllib.request  # Standard library, no need for pip install, not as good as requests!


def is_up(url, retries=5):  # We can pass any website as argument into our url parameter, retries will coordinate
    # with errors we should keep this as a parameter so user can specify their own criteria for failures
    fails = 0  # we will use this variable to measure each except trigger
    while fails < retries:  # our main loop wil continue running unless we trigger 5 exceptions
        try:
            urllib.request.urlopen(url)  # if this request is successful continue through block
        except Exception as ex:  # we are catching our exception and storing it inside of e variable
            print(f"{ex} for {url}.. Please check spelling of url!")  # Simple f string printing our ex variable error
            # followed by url
            fails += 1  # because we had an exception, fails will increment by 1
        else:
            print(f"{url} is up and running")  # If except does not trigger we simply output our else statement.
        time.sleep(90)  # We will only run this loop every 90 seconds
    # Your choice to add email notifications after the while loop breaks


if __name__ == "__main__":
    is_up("https://www.facebook.com")

