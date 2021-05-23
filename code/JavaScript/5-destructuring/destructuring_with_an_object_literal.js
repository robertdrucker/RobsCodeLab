myCircle = {
  radius: 10,

  // Getter
  getRadius() {
    return myCircle.radius;
  },

  // Setter
  setRadius(radius) {
    myCircle.radius = radius;
  },

  calcArea() {
    return 3.14 * myCircle.getRadius() ** 2;
  },
};

myCircle.setRadius(5);
console.log(
  `\n\nThe radius of my circle is ${myCircle.getRadius()} square units.`
);
console.log(`The area of my circle is ${myCircle.calcArea()} square units.`);

// Destucturing
// Make getRadius = myCircle.getRadius, etc.
const { getRadius, setRadius, calcArea } = myCircle;

setRadius(8.5);
console.log(`\n\nThe radius of my circle is ${getRadius()} square units.`);
console.log(`The area of my circle is ${calcArea()} square units.\n`);
