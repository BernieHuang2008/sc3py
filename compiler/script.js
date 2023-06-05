l = [
	[62, 56, [
		["whenGreenFlag"],
		["gotoX:y:", 26, -74],
		["hide"]
	]],
	[79,
		182,
		[
			["whenIReceive", "消息1"],
			["setVar:to:", "a", ["randomFrom:to:", 1, 100]],
			["setGraphicEffect:to:", "color", ["readVariable", "a"]],
			["call", "aaa"]
		]
	],
	[379.7,
		15.3,
		[
			["procDef", "aaa", [],
				[], false
			],
			["show"],
			["doRepeat",
				5,
				[
					["doRepeat", 10, [
						["changeXposBy:", 2],
						["createCloneOf", "_myself_"]
					]],
					["changeYposBy:", 1],
					["doRepeat", 10, [
						["changeXposBy:", -2],
						["createCloneOf", "_myself_"]
					]],
					["changeYposBy:", 1]
				]
			],
			["hide"]
		]
	],
	[134,
		357,
		[
			["whenCloned"],
			["heading:", 0],
			["doRepeat", 400, [
				["forward:", 0.5]
			]],
			["setGraphicEffect:to:", "color", ["randomFrom:to:", 1, 100]],
			["heading:", ["randomFrom:to:", 1, 360]],
			["forward:", ["randomFrom:to:", 70, 110]],
			["wait:elapsed:from:", 1],
			["deleteClone"]
		]
	]
]


function parse(obj) {
	if (Array.isArray(obj)) {
		if (typeof obj[0] == 'string') {
			var name = obj[0];
			var paras = obj.slice(1, obj.length);
			for (var j = 0; j < paras.length; j++) {
				paras[j] = parse(paras[j]);
			}
			return {
				type: 'function',
				name: name,
				para: paras
			}
		}
		else {
			var lst = [];
			obj.forEach(script=>{
				lst.push(parse(script));
			})
			return lst;
		}
	} else
		return obj;
}

var listener = {};
function addListener(condition, blocks){
	if(listener[condition] == undefined)
		listener[condition] = [];
	listener[condition].push(blocks);
}


function parse_role(scripts) {
	scripts.forEach(script => {
		script = script[2];	// remove position of the block
		var condition = script[0];
		var blocks = script.slice(1, script.length);
		for (var i = 0; i < blocks.length; i++) {
			blocks[i] = parse(blocks[i]);
		}
		console.log(condition, blocks);
	})
}
