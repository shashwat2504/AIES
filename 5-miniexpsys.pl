# student(nayna).
# student(harshad).

# completed_12th(nayna).
# completed_12th(harshad).

# completed_credits(nayna).
# completed_credits(harshad).

# no_backlog(nayna).
# no_backlog(harshad).

# valid_grade(nayna).
# valid_grade(harshad).

# degree(nayna, engineering).
# degree(harshad, bba).

# eligible(X) :-
#     student(X),
#     completed_12th(X),
#     completed_credits(X),
#     no_backlog(X),
#     valid_grade(X).


# start:-
#     write('Enter Student Name: '),
#     read(X),
#     write('Enter Course: '),
#     read(D),
    
#     eligible(X),
#     degree(X,D),
    
#     write('Student is Eligible for: '),
#     write(D),
#     nl.


% Mini Expert System for Career Recommendation

% Facts
interest(student, programming).
interest(student, mathematics).
interest(student, networking).
interest(student, electronics).

% Rules
career(ai_engineer) :-
    interest(student, programming),
    interest(student, mathematics).

career(network_engineer) :-
    interest(student, networking).

career(embedded_engineer) :-
    interest(student, electronics).

career(software_developer) :-
    interest(student, programming).

% Display recommendations
recommend :-
    career(X),
    write('Recommended Career: '),
    write(X),
    nl,
    fail.

recommend.








swipl
consult('miniexpsys.pl').
recommend.







# ## 

# risk(low).
# risk(medium).
# risk(high).

# goal(safety).
# goal(growth).
# goal(income).

# recommend(low, safety, fixed_deposit).
# recommend(low, income, bonds).
# recommend(medium, growth, mutual_funds).
# recommend(medium, income, bonds).
# recommend(high, growth, stocks).
# recommend(high, income, dividend_stocks).

# start :-
#     write('Enter your risk level : '),
#     read(Risk),
    
#     write('Enter your investment goal : '),
#     read(Goal),

#     recommend(Risk, Goal, Investment),

#     write('Recommended investment: '),
#     write(Investment),
#     nl.