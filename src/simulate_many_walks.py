import polymersim as polsim
import polymerstatistics as polstat
import argparse
import statistics as stats

def generate_walk_lengths(min_length, max_length):
    diff = max_length - min_length
    lengths = []
    for step in range(diff):
        lengths.append(min_length + step)
    return lengths

def calc_mean_clashes(walk_length, number_runs):
    clashes_per_run = []
    for i in range(number_runs):
        polymer_positions = polsim.random_walk(walk_length)
        clashes_per_run.append(polstat.count_clashes(polymer_positions))
    return stats.mean(clashes_per_run)

def main():
    parser = argparse.ArgumentParser(description='Simulate many walks and calculate properties')
    parser.add_argument('min_walk_length', metavar='min_walk_length', type=int, help='Min Number of steps in walk')
    parser.add_argument('max_walk_length', metavar='max_walk_length', type=int, help='Max_Number of steps in walk')
    parser.add_argument('number_runs', metavar='number_runs', type=int, help='Number of runs')
    args = parser.parse_args()

    walk_lengths = generate_walk_lengths(args.min_walk_length, args.max_walk_length)
    clash_means =  [calc_mean_clashes(length, args.number_runs) for length in walk_lengths]

    for len_index in range(len(walk_lengths)):
        out_str = str(walk_lengths[len_index]) + "," + str(clash_means[len_index]) + "," + str(clash_means[len_index]/walk_lengths[len_index])
        print(out_str)

if __name__ == "__main__":
    main()
