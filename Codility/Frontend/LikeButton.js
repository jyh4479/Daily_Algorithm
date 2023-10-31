import {useState} from 'react';

const LikeButton = () => {

    const [liked, setLiked] = useState(false);
    const [count, setCount] = useState(100);

    return (
        <>
            <div>
                <button className={`like-button ${liked && 'liked'}`} onClick={() => setLiked(prev => !prev)}>
                    <span>
                        {'Like | '}
                    </span>
                    <span className={'likes-counter'}>
                       {count + (liked ? 1 : 0)}
                    </span>
                </button>
            </div>
            <style>{`
                .like-button {
                    font-size: 1rem;
                    padding: 5px 10px;
                    color:  #585858;
                }
                .liked {
                    font-weight: bold;
                    color: #1565c0;
                }
            `}</style>
        </>
    );
};

export default LikeButton;