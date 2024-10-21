function clicklikes(button) {
    const likePlusElement = button.parentNode.querySelector('.likeplus');
    let likeCount = parseInt(likePlusElement.textContent);
    likeCount++;
    likePlusElement.textContent = likeCount;
    return true;
  }
  