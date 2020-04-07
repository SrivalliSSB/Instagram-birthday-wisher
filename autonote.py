import pyautogui as pg
def instagram(insta):
	pass
	pg.press('win')
	pg.typewrite('instagram', 0.3)
	pg.press('enter')
	pg.PAUSE = 5
	pg.moveTo(676,58,1)
	pg.PAUSE=2
	pg.click(676, 58, 2, 1,'left')
	pg.PAUSE = 0.5
	pg.typewrite(insta, 0.4)
	pg.PAUSE = 1
	pg.press('enter')
	pg.press('enter')
	pg.PAUSE = 0.5
	pg.click(667, 131, 1, 0, 'left')
	pg.PAUSE = 0.5
	pg.typewrite('Happy birthday', 0.4)
	pg.PAUSE = 1
	pg.moveTo(1088,668,1)
	pg.click(1088, 688, 1, 0, 'left')