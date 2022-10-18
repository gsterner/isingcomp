import polymersim as polsim
import polymerstatistics as polstat
import argparse
import statistics as stats


def main():
    parser = argparse.ArgumentParser(description='Simulate many walks and calculate properties')
    parser.add_argument('walk_length', metavar='walk_length', type=int, help='Number of steps in walk')
    parser.add_argument('number_runs', metavar='number_runs', type=int, help='Number of runs')
    args = parser.parse_args()

    clashes_per_run = []
    for i in range(args.number_runs):
        polymer_positions = polsim.random_walk(args.walk_length)
        clashes_per_run.append(polstat.count_clashes(polymer_positions))

    print(clashes_per_run)
    print("Mean:", stats.mean(clashes_per_run))

if __name__ == "__main__":
    main()
