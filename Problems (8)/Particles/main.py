spin = input()
charge = input()
if spin == '1':
    print('Photon Boson')
elif spin == '1/2':
    if charge == '0':
        print('Neutrino Lepton')
    elif charge == '-1':
        print('Electron Lepton')
    elif charge == '2/3':
        print('Charm Quark')
    elif charge == '-1/3':
        print('Strange Quark')
    else:
        print('bad')
else:
    print('unknown')
