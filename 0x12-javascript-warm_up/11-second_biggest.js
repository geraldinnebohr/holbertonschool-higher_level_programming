#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort();
  console.log(args[args.length - 2]);
}
