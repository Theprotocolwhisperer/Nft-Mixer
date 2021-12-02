from web3 import Web3
from PIL import Image
import sys
web3 = Web3(Web3.HTTPProvider("Your Http provider"))

web3.eth.defaultAccount = 'Account to make querys , public key'
abi = " ABI Of the contract e.g [{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_eggs\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_traits\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_maxTokens\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"approved\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"approved\",\"type\":\"bool\"}],\"name\":\"ApprovalForAll\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"Paused\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"Unpaused\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"MAX_TOKENS\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"MINT_PRICE\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"PAID_TOKENS\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"aliases\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"eggs\",\"outputs\":[{\"internalType\":\"contract EGGS\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"existingCombinations\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"getApproved\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"getPaidTokens\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"getTokenTraits\",\"outputs\":[{\"components\":[{\"internalType\":\"bool\",\"name\":\"isTortoise\",\"type\":\"bool\"},{\"internalType\":\"uint8\",\"name\":\"fur\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"head\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"ears\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"eyes\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"nose\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"mouth\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"neck\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"feet\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"alphaIndex\",\"type\":\"uint8\"}],\"internalType\":\"struct IGoat.TortoiseGoat\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"}],\"name\":\"isApprovedForAll\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"isle\",\"outputs\":[{\"internalType\":\"contract IIsle\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"mintCost\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"bool\",\"name\":\"stake\",\"type\":\"bool\"}],\"name\":\"mint_EGGS\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"bool\",\"name\":\"stake\",\"type\":\"bool\"}],\"name\":\"mint_ETH\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"minted\",\"outputs\":[{\"internalType\":\"uint16\",\"name\":\"\",\"type\":\"uint16\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"ownerOf\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"paused\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"rarities\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"safeTransferFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"_data\",\"type\":\"bytes\"}],\"name\":\"safeTransferFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"approved\",\"type\":\"bool\"}],\"name\":\"setApprovalForAll\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_isle\",\"type\":\"address\"}],\"name\":\"setIsle\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_paidTokens\",\"type\":\"uint256\"}],\"name\":\"setPaidTokens\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bool\",\"name\":\"_paused\",\"type\":\"bool\"}],\"name\":\"setPaused\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes4\",\"name\":\"interfaceId\",\"type\":\"bytes4\"}],\"name\":\"supportsInterface\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"index\",\"type\":\"uint256\"}],\"name\":\"tokenByIndex\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"index\",\"type\":\"uint256\"}],\"name\":\"tokenOfOwnerByIndex\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"tokenTraits\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"isTortoise\",\"type\":\"bool\"},{\"internalType\":\"uint8\",\"name\":\"fur\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"head\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"ears\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"eyes\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"nose\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"mouth\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"neck\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"feet\",\"type\":\"uint8\"},{\"internalType\":\"uint8\",\"name\":\"alphaIndex\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"tokenURI\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"traits\",\"outputs\":[{\"internalType\":\"contract ITraits\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"tokenId\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"whitelist\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"withdraw\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"
address = web3.toChecksumAddress('Address of the contract')
contract = web3.eth.contract(address=address, abi=abi)

tokenid = sys.argv[1] # This is how you pass an argument to the script

print(tokenid)

traits = contract.functions.tokenTraits(int(tokenid)).call()
#print(traits)
#print(len(traits))
#print(traits[0]) #Si identa desde 0
if traits[0] == False:
                iterador0 = traits[8] #Fur tiene 10 para iterar
                iterador1 = str(traits[9]) #Eyes tien 10 para iterar
                iterador2 = traits[4] #Head tiene 10 para iterar
                if iterador2 > 9:
                        if iterador2 == 19:
                                iterador2 = str(1)
                        else:
                                n = iterador2
                                contador = [int(x) for x in str(n)]
                                iterador2 = contador[0]+ contador[1]
                                iterador2 = str(iterador2)
                else:
                        iterador2 = str(iterador2)
                iterador3 = str(traits[2]) #Neck  tien 9 para iterar
                iterador4 = str(traits[1]) #Feet tiene 20 para iterar

                if iterador0 > 9:
                        if iterador0 == 19:
                                iterador0 = str(1)
                        else:
                                n = iterador0
                                contador = [int(x) for x in str(n)]
                                iterador0 = contador[0]+ contador[1]
                                iterador0 = str(iterador0)
                else:
                        iterador0 = str(iterador0)



                layer1 = Image.open("./goat 40x40/Nueva carpeta con elementos 5/"+ iterador4 + ".png")

                        # layer1 = Image.open("./jigsaw/accesorios/" + a +".png")

                layer2 = Image.open("./goat 40x40/Nueva carpeta con elementos 3/"+ iterador1 + ".png")

                layer3 = Image.open("./goat 40x40/Nueva carpeta con elementos 4/"+ iterador3 +".png")

                layer4 = Image.open("./goat 40x40/Nueva carpeta con elementos 2/"+iterador2+".png")

                layer5 = Image.open("./goat 40x40/Nueva carpeta con elementos/"+iterador0+".png")
                layer1.paste(layer2, (0, 0), layer2)
                layer1.paste(layer3, (0, 0), layer3)
                layer1.paste(layer4, (0, 0), layer4)
                layer1.paste(layer5, (0, 0), layer5)

                layer1.save('./output/'+ str(tokenid) + '.png')
                tokenid+=1

else:
                titerador0 = str(traits[1])  # Fur
                titerador1 = traits[2]  # Eyes tiene 9
                titerador2 = str(traits[3])  # Head
                titerador3 = traits[6]  # Neck
                if titerador3 > 9:
                        if titerador3 == 19:
                                titerador3 = str(1)
                        else:
                                n = titerador3
                                contador = [int(x) for x in str(n)]
                                titerador3 = contador[0]+ contador[1]
                                titerador3 = str(titerador3)
                else:
                        titerador3 = str(titerador3)

                titerador4 = traits[8] # Feet

                if titerador1 > 9:
                        if titerador1 == 19:
                                titerador1 = str(1)
                        else:
                                n = titerador1
                                contador = [int(x) for x in str(n)]
                                titerador1 = contador[0]+ contador[1]
                                titerador1 = str(titerador1)
                else:
                        titerador1 = str(titerador1)



                layer1 = Image.open("./tortugas 40x40/Nueva carpeta con elementos 3/"+titerador0+".png")
                layer2 = Image.open("./tortugas 40x40/Nueva carpeta con elementos 5/"+titerador2+".png")
                layer3 = Image.open("./tortugas 40x40/Nueva carpeta con elementos 4/"+titerador1+".png")
                layer4 = Image.open("./tortugas 40x40/Nueva carpeta con elementos/"+titerador3+".png")

                if traits[8] > 9:
                        titerador4 = str(titerador4 - 10)
                else:
                        titerador4 = str(traits[8])


                layer5 = Image.open("./tortugas 40x40/Nueva carpeta con elementos 2/"+titerador4+".png")
                layer1.paste(layer2, (0, 0), layer2)
                layer1.paste(layer3, (0, 0), layer3)
                layer1.paste(layer4, (0, 0), layer4)
                layer1.paste(layer5, (0, 0), layer5)

                layer1.save('./output/'+ str(tokenid) + '.png')
