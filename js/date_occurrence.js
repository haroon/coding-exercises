console.log("--------------------");
for (var year = 2014; year <= 2050; year++) {
  var d = new Date(year, 11, 31);
  if (d.getDay() === 6) console.log("31st December is being a Saturday " + year);
}
console.log("--------------------");
