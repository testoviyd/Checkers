const { expect } = require("chai");

describe("BaseCheckers Contract", function () {
    it("Should set the right owner", async function () {
        const [owner] = await ethers.getSigners();
        const BaseCheckers = await ethers.getContractFactory("BaseCheckers");
        const baseCheckers = await BaseCheckers.deploy();
        await baseCheckers.deployed();

        expect(await baseCheckers.player1()).to.equal(ethers.constants.AddressZero);
    });

    // Additional tests...
});
