// Note the use of the bind method here.
// Binding in this way is an ES6 feature that allows us
// to destructure an instance method without it
// losing its 'this' context.
// IMPORTANT
// If you do not bind 'this', this program will not work.

class Circle {
  constructor() {
    this.radius = 10;
    this.getRadius = this.getRadius.bind(this);
    this.setRadius = this.setRadius.bind(this);
    this.calcArea = this.calcArea.bind(this);
  }
  // Getter
  getRadius() {
    return this.radius;
  }

  // Setter
  setRadius(radius) {
    this.radius = radius;
  }

  calcArea() {
    return 3.14 * this.getRadius() ** 2;
  }
}

myCircle = new Circle(10);

myCircle.setRadius(5);
console.log(
  `\n\nThe radius of my circle is ${myCircle.getRadius()} square units.`
);
console.log(`The area of my circle is ${myCircle.calcArea()} square units.`);

// Destructuring
// Make getRadius = myCircle.getRadius, etc.
const { getRadius, setRadius, calcArea } = myCircle;

setRadius(8.5);
calcArea();
console.log(`\n\nThe radius of my circle is ${getRadius()} square units.`);
console.log(`The area of my circle is ${calcArea()} square units.\n`);
