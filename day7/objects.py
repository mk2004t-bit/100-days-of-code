hangman_title = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                     
                    |___/                      
"""
words = [
    "anchor", "antenna", "backpack", "ball", "balloon", "barrel",
    "basket", "battery", "bed", "bell", "belt", "bench",
    "bicycle", "bin", "blanket", "blender", "book", "bookmark",
    "boots", "bottle", "bowl", "box", "bracelet", "brick",
    "bridge", "broom", "brush", "bucket", "button", "cable",
    "calculator", "calendar", "camera", "candle", "cannon", "cap",
    "car", "card", "carpet", "cart", "case", "chain",
    "chair", "chalk", "charger", "chest", "clock", "closet",
    "coat", "coin", "comb", "compass", "computer", "container",
    "couch", "cup", "curtain", "cushion", "desk", "diamond",
    "diary", "door", "drawer", "drill", "drum", "dustbin",
    "earphones", "envelope", "eraser", "fan", "faucet", "feather",
    "fence", "file", "flag", "flashlight", "folder", "fork",
    "frame", "fridge", "funnel", "furniture", "gamepad", "gate",
    "generator", "glasses", "globe", "gloves", "guitar", "hammer",
    "hanger", "hat", "headphones", "helmet", "hook", "hose",
    "hourglass", "iron", "jar", "jewel", "jug", "kettle",
    "key", "keyboard", "knife", "ladder", "lamp", "lantern",
    "laptop", "lock", "magnet", "mailbox", "map", "marker",
    "mask", "mat", "medal", "mirror", "mobile", "monitor",
    "mug", "nail", "necklace", "needle", "net", "newspaper",
    "notebook", "oven", "package", "paintbrush", "palette", "paper",
    "pen", "pencil", "phone", "piano", "picture", "pillow",
    "pipe", "plate", "pliers", "pocket", "pot", "printer",
    "projector", "purse", "radio", "razor", "remote", "ring",
    "robot", "rope", "router", "ruler", "saddle", "safe",
    "saw", "scarf", "scissors", "screw", "screwdriver", "screen",
    "shield", "shirt", "shoe", "shovel", "sink", "skateboard",
    "soap", "socket", "sofa", "spade", "speaker", "spoon",
    "stapler", "statue", "stove", "suitcase", "sunglasses", "sword",
    "table", "tablet", "television", "tent", "thermometer", "thread",
    "ticket", "tire", "toolbox", "toothbrush", "torch", "towel",
    "toy", "tractor", "train", "trashcan", "trophy", "truck",
    "umbrella", "vacuum", "vase", "violin", "wallet", "wardrobe",
    "watch", "waterfall", "webcam", "wheel", "whistle", "window",
    "wire", "wrench", "zipper"
]

hangman = [
    # 6 lives
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",

    # 5 lives
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

    # 4 lives
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

    # 3 lives
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

    # 2 lives
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",

    # 1 life
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",

    # 0 lives
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
