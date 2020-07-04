import argparse
import focusedme


def main():
    """ parse cli arguments and start sequence of object calls"""

    print(focusedme.BANNER, "\n")
    print(" __ A Pomodoro Timer ___" + "\n\n")
    parser = argparse.ArgumentParser(
        description="Welcome to the focusedMe app. Start your Pomodoro timer"
        " and enjoy the focus! (Stop it with Ctrl+c)",
        usage="%(prog)s [-f] [-sb] [-lb] [-r]",
    )
    parser.add_argument(
        "-r",
        "--num_rounds",
        type=int,
        metavar="",
        help="number of rounds, default is 3",
    )
    parser.add_argument(
        "-f",
        "--focus_time",
        type=int,
        metavar="",
        help="duration in minutes of the focus session, default is 25 mins",
    )
    parser.add_argument(
        "-sb",
        "--short_break",
        type=int,
        metavar="",
        help="duration in minutes of the short break, default is 5 mins",
    )
    parser.add_argument(
        "-lb",
        "--long_break",
        type=int,
        metavar="",
        help="duration in minutes of the focus session, default is 25 mins",
    )

    args = parser.parse_args()
    # dictionary that store Pomodor initialization parameters
    len_args = focusedme.LENGHT_ARGS
    num_rounds = focusedme.NUM_ROUNDS
    if args.focus_time:
        len_args["focus_time"] = args.focus_time
    if args.short_break:
        len_args["short_break"] = args.short_break
    if args.long_break:
        len_args["long_break"] = args.long_break
    if args.num_rounds:
        num_rounds = args.num_rounds

    # initialize view
    view = focusedme.View()
    # start pomodoro
    view.run(len_args, num_rounds)


if __name__ == "__main__":
    main()