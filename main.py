from festival_scheduler import FestivalScheduler
from plot import plot_stages

def main() -> None:
    fs = FestivalScheduler()
    fs.schedule()
    plot_stages(fs.stages)

if __name__ == "__main__":
    main()