import React from 'react';

import TopStories from './TopStories';
import Card from './Card';
import Footer from './Footer';

const HomePage = () => {
    return (
        <div className="flex flex-col w-full overflow-x-hidden">
            <div>
                <TopStories />
            </div>
            <div className="w-full flex flex-row justify-center mt-5 py-10">
                <div className="flex flex-col w-1/2">
                    <Card />
                    <Card />
                    <Card />
                </div>
                <div className="w-1/4 bg-black">
                    <h1>
                        ads
                    </h1>
                </div>
            </div>
            <div>
                <Footer />
            </div>
        </div>
    );
}

export default HomePage;