import React from "react";

const Header = () => {
    return (
        <div className="w-full h-[4rem] border-b border-black 
            flex flex-row justify-between px-[5rem] items-center shadow-md"
        >
            <div>
                <h1>Logo</h1>
            </div>
            <div className="flex flex-row gap-10">
                <h3>category</h3>
                <h3>category</h3>
                <h3>category</h3>
            </div>
        </div>
    );
};

export default Header;