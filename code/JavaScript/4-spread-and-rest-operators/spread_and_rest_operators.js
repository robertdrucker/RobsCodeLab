// The spread operator used to extract
// all elements from an array
const albumsListOne = ['Let it Bleed', 'Abbey Road', 'Houses of the Holy'];
const albumsListTwo = ['Tusk', 'All Things Must Pass', 'Octave'];

const allAlbums = [...albumsListOne, ...albumsListTwo, 'Book of Dreams'];

console.log('\nAll albums:');
console.log(allAlbums);

// The spread operator used to extract
// all properties from an object
const partialProfile = {
  name: 'Greg Park',
  occupation: 'electrician',
};

const fullProfile = {
  ...partialProfile,
  age: 28,
};

console.log('\nFull profile:');
console.log(fullProfile);

// The rest operator merges a list of function arguments into an array.
// ...args must be the last formal argument because it collects
// all of the remaining arguments.

const names = (manager, leader, ...args) => {
  console.log('\nargs:');
  console.log(args);
  console.log('\nmanager:');
  console.log(`${manager}\n`);
};

names('Susan', 'Kate', 'Janis', 'David', 'Mike');
