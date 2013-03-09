
var roll = 27;

var niccokick = {
	turn27: function(rock) {
		var rockNRollHeaven;
		if (rock * 2 + 1 === 27) {
			rockNRollHeaven = 'YEAH!';
		} else {
			rockNRollHeaven = 'too bad';
		}
		return { rockNRollHeaven: rockNRollHeaven };
	}
};

module.exports.niccokick = niccokick;
