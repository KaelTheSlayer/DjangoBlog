﻿var groupmates = [
	{
	"name" : "Василий",
	"group": "912-2",
	"age": 19,
	"marks": [4,3,5,5,4]
	},
	{
	"name" : "Анна",
	"group": "912-1",
	"age": 18,
	"marks": [3,2,3,4,3]
	},
	{
	"name" : "Георгий",
	"group": "912-2",
	"age": 19,
	"marks": [3,5,4,3,5]
	},
	{
	"name" : "Валентина",
	"group": "912-1",
	"age": 18,
	"marks": [5,5,5,4,5]
	}
];

var rpad = function(str,length) {
	str.toString();
	while (str.length < length)
		str=str + ' ';
	return str;
};
var sortbygroup = function(students,group_sort)
{
	console.log(
		rpad("Имя студента", 15),
		rpad("Группа", 8),
		rpad("Возраст", 8),
		rpad("Оценки", 20)
		);
	for (var i=0;i<=students.length-1;i++)
	{
   if (groupmates[i]['group']==group_sort){
		console.log(
		rpad(students[i]['name'], 15),
		rpad(students[i]['group'], 8),
		rpad(students[i]['age'], 8),
		rpad(students[i]['marks'], 20));
    };
	};
console.log('\n');
};
sortbygroup(groupmates,'912-2');