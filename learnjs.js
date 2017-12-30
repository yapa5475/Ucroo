//node learnjs.js

var skills = ["awesomeness", "programming", "teaching", "JS"];
console.log(skills[0])
console.log(skills)

//there are no classes in js, only objects

//object literal notation
var bio = {
	"name" : "Yash Parekh",
	"age" : 22,
	"role" : "Developer",
	"skills" : skills,
	"contacts" : {
		"mobile" : "303-949-6756",
		"email" : "yash.parekh223@gmail.com",
		"github" : "yapa5475",
		"location" : "Aurora"
	},
	"welcomeMessage" : "Hello my name is Yash!"
};

bio.favoritecolor = "blue"