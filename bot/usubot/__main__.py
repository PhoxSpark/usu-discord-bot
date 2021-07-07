import main
import logs
import args

logger = logs.setup('usubot')

if __name__ == "__main__":
    args = args.parse_arguments()
    main.start(args)
