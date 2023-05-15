#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		int fib(int);
		double getDecades();

	private:
		int age;
		int _fib(int);
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

int Person::fib(int n){
	return _fib(Person::getAge());

}

int Person::_fib(int n){ 
	if (n<=1){
		return n;
	}

	else {
		return (fib(n-1) + fib(n-2));
	}
}


double Person::getDecades(){
	return age/10.0;
	}


extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	int Person_fib(Person* person) {person->fib();}
	double Person_getDecades(Person* person) {return person->getDecades();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}