#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const nums = [];
  for (let i = 0; i < (process.argv.length - 2); i++) {
    nums[i] = parseInt(process.argv[i + 2]);
  }
  nums.sort(function sortNum (a, b) { return a - b; });
  console.log(nums);
  console.log(nums[nums.length - 2]);
}
