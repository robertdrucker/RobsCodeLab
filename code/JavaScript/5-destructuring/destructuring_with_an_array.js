// Destructuring used with an array
const assignedBooks = [
  'The Great Gatsby',
  'To Kill a Mockingbird',
  'Nineteen Eighty-Four',
];

// Destructuring
// Make book1 = assignedBooks[0], etc.
const [book1, book2, book3] = assignedBooks;

console.log('\nBooks to read:');
console.log(`Book 1: ${book1}`);
console.log(`Book 2: ${book2}`);
console.log(`Book 3: ${book3}\n`);
