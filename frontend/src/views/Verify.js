import React, { useEffect, useState } from 'react';
import Loader from '../components/Loader/Loader';
import API from '../shared/api';
import ViewWrappers from '../components/ViewWrappers/ViewWrappers';
import { useUserContext } from '../context/UserContext';

function Verify({ match, history }) {
  const [isVerified, setIsVerified] = useState(0);
  const { id, token } = match.params;
  const { setVerified } = useUserContext();

  useEffect(() => {
    (async () => {
      if (id && token) {
        try {
          await API.verify.post({ user_id: id, verification_key: token});
          setIsVerified(1);
          setVerified(true);
        }
        catch (e) {
          console.error(e);
          setIsVerified(-1);
        }
      }
    })(); // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (isVerified)
      setTimeout(() => history.push('/stores/new/business'), 5000);
  }, [history, isVerified]);

  return (
    <ViewWrappers.View withPadding>
      <div className="Intro">
        {!isVerified && <Loader/>}
        {isVerified === 1 && <><h1>Successfully verified</h1><p>Everything good. You will be redirected in five seconds.</p></>}
        {isVerified === -1 && <h1>Something went wrong.</h1>}
      </div>
    </ViewWrappers.View>
  )
}

export default Verify;
