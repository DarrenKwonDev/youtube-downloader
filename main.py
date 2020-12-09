from pytube import YouTube


candidate = [
    # ... url 넣기
]

for i in candidate:
    yt = YouTube(i)
    print(yt.title, yt.length)

    yt_streams = yt.streams
    # YouTube 객체인 yt에서 stream 객체를 생성

    # print("다운가능한 영상 상세 정보 :")
    # for i, stream in enumerate(yt_streams.all()):
    #     print(i, " : ", stream)

    # acodec과 vcodec 둘 다 있어야 음성, 비디오가 동시에 있는 것을 선택 가능함
    for i, stream in enumerate(yt_streams.filter(progressive=True, file_extension='mp4').all()):
        print(i, stream)

    print(" \"itag\"를 이용해 특정 stream 선택 :")
    itag = input()  # 재생 목록이라면 보통 itag가 같으니 하나만 출력해보고 고정값으로 할당하는게 좋음
    my_stream = yt_streams.get_by_itag(itag)
    print("선택된 stream: ", my_stream)

    print("선택된 stream 다운로드")
    my_stream.download()
