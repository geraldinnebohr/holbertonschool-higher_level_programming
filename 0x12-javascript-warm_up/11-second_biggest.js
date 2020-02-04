#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const intArgs = args.map(function (x) {
    return parseInt(x, 10);
  });
  intArgs.sort();
  console.log(args[args.length - 2]);
}
