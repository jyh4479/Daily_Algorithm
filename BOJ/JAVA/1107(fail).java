import sys


def selectNumber(numberList, selectedNumber, sel, cnt):
		global ans, channel, N
		if sel == cnt:
		if len(selectedNumber) != 1 and selectedNumber[0] == '0':
		selectedNumber = selectedNumber[1:]
		# print(int(selectedNumber))
		ans = min(ans, abs(channel - 100))
		ans = min(ans, len(selectedNumber) + abs(channel - int(selectedNumber)))

		else:
		for i in range(len(numberList)):
		selectedNumber += str(numberList[i])
		selectNumber(numberList, selectedNumber, sel, cnt + 1)
		selectedNumber = selectedNumber[:-1]


		if __name__ == '__main__':
		ans = sys.maxsize
		channel = input()
		N = int(input())
		numberList = [i for i in range(10)]
		if N != 0:
		removeNumberList = map(int, input().split())
		for data in removeNumberList:
		numberList.remove(data)

		# print(numberList)
		channelSize = len(channel)
		channel = int(channel)

		for i in range(channelSize):
		selectNumber(numberList, '', i + 1, 0)

		print(ans)
