class Person {
	constructor(name) {
		this.name = name;
	}

	sayHi() {
		alert("Hello, I'm " + this.name)
	}

}

let p = new Person("Martin");
p.sayHi();
