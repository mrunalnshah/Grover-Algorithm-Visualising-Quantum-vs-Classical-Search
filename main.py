# Author : Mrunal Nirajkumar Shah

# MAIN FUNCTION

from src.comparison import search_comparison

def main():
    search_comparison(10, 5, "1")
    search_comparison(50, 49, "2")
    search_comparison(50, 80, "3")
    search_comparison(256, 108, "4")
    search_comparison(1000, 555,"5")
    search_comparison(1000, 1001, "6")

if __name__ == "__main__":
    main()