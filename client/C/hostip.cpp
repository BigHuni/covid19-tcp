#define _CRT_SECURE_NO_WARNINGS
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib, "ws2_32")
#include <WinSock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <io.h> // _open(), _read() 사용하기 위해서
#include <fcntl.h> // O_CREATIO, _O_RDONLY 사용하기 위해
#include <sys/types.h>
#include <errno.h>
#include <sys/stat.h> // _S_IWRITE 사용하기 위해

#define PORT	8081
#define MAXBUF	1024

int main(int argc, char* argv[]) {
	WSADATA		WSAData;
	SOCKADDR_IN addr;
	SOCKET		s;
	char buffer[1024];
	char file_name[13] = "covid19.json";
	int i;
	int len = 0;
	int dest_fd;
	int recv_len;
	int totaln = 0;

	char* hostname = argv[1];
	char ip[100];
	struct hostent* he;
	struct in_addr** addr_list;

	printf("\nInitialising Winsock...");
	if (WSAStartup(MAKEWORD(2, 2), &WSAData) != 0)
	{
		printf("Failed. Error Code : %d", WSAGetLastError());
		return 1;
	}

	printf("Initialised.\n");


	if ((he = gethostbyname(hostname)) == NULL)
	{
		//gethostbyname failed
		printf("gethostbyname failed : %d", WSAGetLastError());
		return 1;
	}

	addr_list = (struct in_addr**)he->h_addr_list;

	for (i = 0; addr_list[i] != NULL; i++)
	{
		strcpy(ip, inet_ntoa(*addr_list[i]));
	}

	printf("%s IP : %s\n", hostname, ip);
	const char* IP = (ip);

	if (WSAStartup(MAKEWORD(2, 2), &WSAData) != 0) {
		return 1;
	}

	s = socket(AF_INET, SOCK_STREAM, 0);

	if (s == INVALID_SOCKET) {
		return 1;
	}

	addr.sin_family = AF_INET;
	addr.sin_port = htons(PORT);
	addr.sin_addr.S_un.S_addr = inet_addr(IP);
	if (connect(s, (struct sockaddr*)&addr, sizeof(addr)) == SOCKET_ERROR) {
		printf("fail to connect\n");
		closesocket(s);
		return 1;
	}

	send(s, file_name, len, 0);

	// 파일 생성
	dest_fd = _open(file_name, _O_CREAT | _O_EXCL | _O_WRONLY, _S_IWRITE);
	if (!dest_fd) {
		perror("Error ");
		return 1;
	}


	if (errno == EEXIST) {
		printf("File already exist!");
		_close(dest_fd);
		return 1;
	}
	printf("mkfile complete\n");


	while (1) {
		memset(buffer, 0x00, MAXBUF);
		recv_len = recv(s, buffer, MAXBUF, 0);
		if (recv_len == 0) {
			printf("finish file\n");
			break;
		}
		totaln += _write(dest_fd, buffer, recv_len);
	}
	_close(dest_fd);

	closesocket(s);
	WSACleanup();

	return 0;

}