def solution(book_time):

    def change_min(str_time: str) -> int: return int(str_time[0:2]) * 60 + int(str_time[3:])
    
    book_times = sorted([[change_min(book[0]), change_min(book[1]) + 10] for book in book_time])
	
    rooms = []
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[index] = room + book_time
                break
        else: rooms.append(book_time)
    return len(rooms)