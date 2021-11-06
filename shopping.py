buidjet = float(input())
broi_videokarti = int(input())
broi_procesori = int(input())
broi_ram_pamet = int(input())

cost_videokarti = broi_videokarti*250
cost_procesori = cost_videokarti*0.35*broi_procesori
cost_ram_pamet = cost_videokarti*0.1*broi_ram_pamet

total = cost_videokarti+cost_procesori+cost_ram_pamet

if broi_videokarti > broi_procesori:
    total = total - total*0.15

if buidjet >= total:
    print(f'You have {buidjet-total:.2f} leva left!')
else:
    print(f'Not enough money! You need {total-buidjet:.2f} leva more!')