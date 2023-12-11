a = 10;

if a > 0 then
    disp("a is positive");
elseif a == 0 then
    disp("a is zero");
else
    disp("a is negative");
end



choice = 3;

switch choice
    case 1
        disp("You chose option 1")
    case 2
        disp("You chose option 2")
    case 3
        disp("You chose option 3")
    otherwise
        disp("Invalid choice")
end




for i = 1:5
    disp("Current iteration: " + string(i));
end




count = 1;
while count <= 5
    disp("Current count: " + string(count));
    count = count + 1;
end





for i = 1:10
    if i == 5 then
        break;
    elseif i == 3 then
        continue;
    end
    disp("Current iteration: " + string(i));
end
