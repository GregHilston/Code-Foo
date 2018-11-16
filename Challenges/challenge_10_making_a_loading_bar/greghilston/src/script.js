const oneSecondMiliSeconds = 1000
let progressBar = document.getElementById("progress") 
let resetLoadingBarButton = document.getElementById("setload")
let intervalRef
let loadTimeMiliSeconds
let timeToRunMiliSeconds = 0


resetLoadingBarButton.addEventListener("click", resetLoadingBarButtonClicked)

/**
 * Resets the internal counter for how much time has elapsed and visuall resets
 * the progress bar.
 */
function resetProgressBar() {
    progressBar.style.width = 0
    timeElapsedMiliseconds = 0
}

/**
 * If a reoccurring progress function is occuring, cancels it.
 */
function stopProgressBar() {
  if(intervalRef) {
    clearInterval(intervalRef)
  }
}

/**
 * Advances internal time state and visualization by one second of progress
 */
function advanceProgressBarOneSecond() {
    const percentageConversionFromRatio = 100

    timeElapsedMiliseconds += oneSecondMiliSeconds

    progressBar.style.width = (timeElapsedMiliseconds / timeToRunMiliSeconds) * percentageConversionFromRatio + "%"

    if(progressBar.style.width == "100%") {
      clearInterval(intervalRef)
    }
}

/**
 * Starts the progress bar reoccurring function
 */
function startProgressBar(timeToRunMiliSeconds) {
  intervalRef = setInterval(advanceProgressBarOneSecond, oneSecondMiliSeconds)
}

/**
 * Stops any previous progress bar code, resetting the state and starting again. Called on "Reset Loading Bar" click
 */
function resetLoadingBarButtonClicked() {
    timeToRunMiliSeconds = document.getElementById("secondsinput").value * oneSecondMiliSeconds

    stopProgressBar()
    resetProgressBar()
    startProgressBar()
}