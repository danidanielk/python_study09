
create table weather(
w_no number(3) primary key,
w_hour varchar2(20char),
w_temp varchar2(20char)
);

create sequence weather_seq;
select * from weather;

create table weather__15(
w_name varchar2(20char),
w_pm10 number(5),
w_pm25 number(5)
);

select * from weather__15;





---------------------------------
--학생(이름,생일,강의장번호,중간고사점수,기말고사점수)
create table student_1115 (
s_no number(10) primary key,
s_name varchar2(20char) not null,
s_birthday date not null,
s_room number(10) not null,
s_midle_score number(10) not null,
s_last_score number(10) not null
);

select * from student_1115;
create sequence student_1115_seq;
---------------------------------
--강의장 (강의장 번호, 위치)
create table room_1115 (
r_no number(10) primary key,
r_location varchar2(30char) not null
);

insert into room_1115 values(1,'7층복도 오른쪽');
insert into room_1115 values(2,'7층복도 왼쪽');
insert into room_1115 values(3,'7층복도 첫번째');
insert into room_1115 values(4,'8층 왼쪽');
insert into room_1115 values(5,'6층 오른쪽');